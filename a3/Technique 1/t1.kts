import java.io.File
import java.io.Writer

fun getAbsolutePathPrefix(file: File, includePath: String, relativeTo: File): String {
    if ("ecpg" in file.path) {
        val isInEcpgIncludes = File("${relativeTo}/postgresql-13.4/src/interfaces/ecpg/include")
            .walkTopDown()
            .any { includePath in it.path }

        if (isInEcpgIncludes) {
            return "postgresql-13.4/src/interfaces/ecpg/include/$includePath"
        }
    }

    val isInRegularIncludes = File("${relativeTo}/postgresql-13.4/src/include")
        .walkTopDown()
        .any { includePath in it.path }

    if (isInRegularIncludes) {
        return "postgresql-13.4/src/include/$includePath"
    }

    val nPaths = includePath.frequencyOf('/')
    return "${file.parentFile(level = nPaths + 1).toRelativeString(relativeTo)}/$includePath";
}

val regex = Regex("#include \"(.*)\"")

fun parseLine(line: String, file: File, writer: Writer, relativeTo: File) {
    val matchResult = regex.find(line)
    if (matchResult != null) {
        val (includeFile) = matchResult.destructured

        val path = getAbsolutePathPrefix(file, includeFile, relativeTo)

        writer.appendLine("cLinks ${file.toRelativeString(relativeTo)} $path")
    }
}

val outputFile = File(args[1])
val relativeTo = File(args[0])

outputFile.writer().use { writer ->
    writer.appendLine("FACT TUPLE :")

    File("${args[0]}/postgresql-13.4").walkTopDown()
        .filter(File::isFile)
        .filter { it.extension == "c" || it.extension == "h" }
        .take(100)
        .forEach {
            writer.appendLine("\$INSTANCE ${it.toRelativeString(relativeTo)} cFile")
            it.forEachLine { line -> parseLine(line, it, writer, relativeTo) }
        }
}

/**
 * Returns the number of occurrences of the given [char] in [this] string.
 */
fun String.frequencyOf(char: Char): Int = this.count { it == char }

/**
 * Returns the nth level parent of this file. A [level] of 0 returns [this] file.
 */
fun File.parentFile(level: Int): File {
    var file = this
    for (i in 0 until level) {
        file = file.parentFile
    }
    return file
}
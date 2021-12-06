# PostgreSQL Dependency Extraction

This technique parses the source code files of Postgres to export its dependencies.

## Usage

Ensure you have Kotlin installed. Then, run:


```
kotlinc -script t1.kts -- <source> <output>
```
where `<source>` is the path to the directory where the PostgreSQL directory is located, and `<output>` is the path to the output TA file.
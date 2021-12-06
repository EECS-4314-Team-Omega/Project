import os
import glob
def printDeps(filename):
    
    with open(filename, 'r') as f:
        file_deps = f.readlines()
        count = 0
        dependee=""
        for dep in file_deps: 
            line_dependencies = dep.strip().split(" ")
            
            for dependency in line_dependencies: 
                
                if count==1: 
                    #dependee is the one that depends on others
                    #dependee = dependency
                    #altered_filename is for the dependee
                    
                    altered_filename = "postgresql-13.4/"+(filename[19:-1]).replace('\\','/')+"c"
                    #altered_filename = dependency
                    dependee = altered_filename
                    print("$INSTANCE "+altered_filename+" cFile") 
                      
                    
                else: 
                    if(count>1 and dependency!="\\"):
                        
                        cleanedDependency = dependency.strip()
                        actualDependeeFilepath = os.path.join("./","../postgresql-13.4.tar/postgresql-13.4/",dependee)
                        actualDependeeFolder = os.path.abspath(os.path.join(actualDependeeFilepath,"../")) #Dependee folder technically exists one layer above the given filepath
                        formattedDependency = os.path.abspath(os.path.join(actualDependeeFolder,cleanedDependency))
                        
                        
                        last_dots = cleanedDependency.rfind("../")
                        
                        
                        #Cleaned dependency is the relative filepath. formattedDependency is the absolute path
                        #print(actualDependeeFilepath+","+cleanedDependency+","+formattedDependency)
                        #print(dependee+","+formattedDependency[53:].replace("\\","/"))
                        
                        print("cLinks "+dependee+" "+formattedDependency[74:].replace("\\","/")) 
                        
                count+=1
                
            
      
    ##print(file_deps)

def main():
    
    print("FACT TUPLE :")
    dependencyFiles = glob.glob('..\\dependencyfiles'+'\**\*.d',recursive=True)
    
    for file in dependencyFiles:
        printDeps(file)

if __name__=="__main__":
   main()

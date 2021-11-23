import os

pwd = "/home/maxim/justNode/tedit/"
res = pwd+"debug/res.txt"
current_path_to_file = ""

file = open(res,"w")
file.write("")
file.close()



while True:
    file = open(res,'r') 

    resContent =  file.readlines()


    
    if os.path.isdir(os.getcwd()):
        
        if len(resContent) != 0:      

            command = ""
            for el in resContent:

                if el.find("exit") != -1:
                    exit()

                elif el.find("..") != -1:
                    command = "../"
            
            
            
            if command == "../":
                file = open(res,"w")
                file.write(os.getcwd())
                file.close()
        
            print(os.getcwd())
                
            if os.path.isdir(os.getcwd() + f"/{resContent[0]}"):        
                os.chdir(resContent[0])
                file = open(res,"w")
                file.write(os.getcwd())
                file.close()
                os.system(f"node {pwd}main.js")
            else:

                file = open(os.getcwd() +f"/{resContent[0]}","r")
                for line in file.readlines():
                    print(line)
                file.close()

                file = open(res,"w")
                file.write(os.getcwd())
                file.close()


                os.system(f"node {pwd}main.js")
        
        else :
            
            file = open(res,"w")
            file.write(os.getcwd())
            file.close()

            
            os.system(f"node {pwd}main.js")
    
    else :
        file = open(res,"w")
        file.write(os.getcwd())
        file.close()

        os.system(f"node {pwd}main.js")
    

    



    file = open(res,"r")
    data = file.read()
    if len(data) > 100:

        exit()
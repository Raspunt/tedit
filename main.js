let term = require( 'terminal-kit' ).terminal ;
let fs = require('fs')

let pwd = "/home/maxim/justNode/tedit/"
let res = pwd+"debug/res.txt"


let pathToFile = fs.readFileSync(res)
console.log(String(pathToFile))

if (fs.lstatSync(String(pathToFile)).isDirectory()){

    let items = readCurrnentDir(String(pathToFile))
    
    term.singleColumnMenu( items , function( error , response ) {
        term( '\n' ).eraseLineAfter.green(
            "#%s selected: %s (%s,%s)\n" ,
            response.selectedIndex ,
            response.selectedText ,
            response.x ,
            response.y
            ) ;
            
            if (response.selectedText == "exit"){
                fs.writeFileSync(res,`exit ${response.selectedText}`)
            }else{
                fs.writeFileSync(res,response.selectedText)
            }
            
            
            
            process.exit() ;
        } ) ;
        
}else {
    fs.writeFileSync(res,res)    
    
    process.exit()
}
        
    
    
function readCurrnentDir(pathToDir){
        
    let listDir = []
    listDir.push("exit")
    listDir.push("..")
    fs.readdirSync(pathToDir).forEach(file => {
        listDir.push(file);
    });
    
    return listDir
}
#!/usr/bin/node
// writing on  file
const fs = request('fs');
fs.writeFile(process.argv[2],process.argv[3],'utf-8', function(error,data){
if(error){
	console.log(error)
}	
});


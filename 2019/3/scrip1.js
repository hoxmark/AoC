console.log("Don")
var wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
var wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']


var size = 10
var grid = new Array(size); 
console.log(grid);


for (var i = 0; i < size; i++) { 
    grid[i]=new Array(size)
    for (var j = 0; j < size; j++) { 
        grid[i][j] = '.'
    }
}

var x = 0 
var y = 0 
grid[x,y] = 'O'

function a(wire){
    wire.forEach(element => {
        let direction = element[0]
        let len = element.slice(1)
        
        switch (direction) {
            case 'L':
                new_x = x-len
                grid.forEach(element => {
                    element[y]
                });
                     
                break;
            case 'R':
                x = x+len    
                break;
            case 'U':
                y = y+len
                break;
            case 'D':
                y = y-len  
                break;            
            default:
                break;
        }
        
    });
}


a(wire1)


for (var i = 0; i < size; i++) { 
    var line = ""
    for (var j = 0; j < size; j++)    { 
        line += grid[i][j] + " "; 
    } 
    console.log(line); 
}  



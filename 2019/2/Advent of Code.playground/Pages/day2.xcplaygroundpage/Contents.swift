import Cocoa
//--- Day 2: 1202 Program Alarm ---

var input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]

func compute(main_memory: inout [Int], instruction: [Int]) -> Bool? {
    let opcode = instruction[0]
    
    switch opcode {
    case 1:
        let pos_a = instruction[1]
        let pos_b = instruction[2]
        let pos_ans = instruction[3]
        main_memory[pos_ans] = main_memory[pos_a] + main_memory[pos_b]
        return false
        
    case 2:
        let pos_a = instruction[1]
        let pos_b = instruction[2]
        let pos_ans = instruction[3]
        main_memory[pos_ans] = main_memory[pos_a] * main_memory[pos_b]
        return false
    case 99:
        //print("Halting app")
        return true
    default:
        //print("ERRORR")
        return true
    }
}

func start_computer(inp:[Int], noun: Int, verb : Int) -> Int{
    var memory = inp
    memory[1] = noun
    memory[2] = verb
    
    for instruction_pointer in stride(from: 0, to:memory.count, by: 4) {
        let sub_codes = Array(memory[instruction_pointer...(instruction_pointer+3)])
        
        if let error = compute(main_memory:&memory, instruction:sub_codes) {
            //print("error", error, instruction_pointer)
            if error {
                return memory[0]
                //print("Answer", memory[0])
            }
        }
    }
    //print(memory)
    return -1
}


let gravity = 19690720
//let gravity = 3516593

func check_combinations(g : Int){
    for i in 0...99 {
        for j in 0...99 {
            let ans = start_computer(inp: input, noun: i, verb: j)
            //print(i, j, ans)
            if (ans == g){
                print("i: ", i)
                print("j: ", j)
                return
            }
            if (ans > gravity){
                break
            }
        }
    }
}

//check_combinations(g:gravity)
//start_computer(inp: input, noun: 77, verb: 49)
start_computer(inp: input, noun: 12, verb: 2)

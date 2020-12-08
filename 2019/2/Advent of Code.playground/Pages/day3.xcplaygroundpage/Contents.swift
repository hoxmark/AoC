//: [Previous](@previous)

import Foundation

extension String {
  subscript (i: Int) -> Character {
    return self[index(startIndex, offsetBy: i)]
  }
  subscript (bounds: CountableRange<Int>) -> Substring {
    let start = index(startIndex, offsetBy: bounds.lowerBound)
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[start ..< end]
  }
  subscript (bounds: CountableClosedRange<Int>) -> Substring {
    let start = index(startIndex, offsetBy: bounds.lowerBound)
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[start ... end]
  }
  subscript (bounds: CountablePartialRangeFrom<Int>) -> Substring {
    let start = index(startIndex, offsetBy: bounds.lowerBound)
    let end = index(endIndex, offsetBy: -1)
    return self[start ... end]
  }
  subscript (bounds: PartialRangeThrough<Int>) -> Substring {
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[startIndex ... end]
  }
  subscript (bounds: PartialRangeUpTo<Int>) -> Substring {
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[startIndex ..< end]
  }
}
extension Substring {
  subscript (i: Int) -> Character {
    return self[index(startIndex, offsetBy: i)]
  }
  subscript (bounds: CountableRange<Int>) -> Substring {
    let start = index(startIndex, offsetBy: bounds.lowerBound)
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[start ..< end]
  }
  subscript (bounds: CountableClosedRange<Int>) -> Substring {
    let start = index(startIndex, offsetBy: bounds.lowerBound)
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[start ... end]
  }
  subscript (bounds: CountablePartialRangeFrom<Int>) -> Substring {
    let start = index(startIndex, offsetBy: bounds.lowerBound)
    let end = index(endIndex, offsetBy: -1)
    return self[start ... end]
  }
  subscript (bounds: PartialRangeThrough<Int>) -> Substring {
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[startIndex ... end]
  }
  subscript (bounds: PartialRangeUpTo<Int>) -> Substring {
    let end = index(startIndex, offsetBy: bounds.upperBound)
    return self[startIndex ..< end]
  }
}


//let test = "123456"
//print(test[0])


let lower_limit = 125730;
let upper_limit = 579381;

//let lower_limit = 111100;
//let upper_limit = 111112;
var res = [Int]();
var counter = 0;
for i in lower_limit...upper_limit{
    let number = String(i)
    
    //1 It is a six-digit number
    //by default
    //if (number.count < 6){
    //    break
    //}
    //2 The value is within the range given in your puzzle input.
    //done by the loop
    
    //Two adjacent digits are the same (like 22 in 122345).
    var no_double = true
    var no_decrease_to_right = true
    for loc in 0..<(number.count-1){
        //print(Int(String(number[loc])), number[loc+1])
        let a = Int(String(number[loc]))
        let b = Int(String(number[loc+1]))

        if (a == b){
            no_double = false
        }
        
        //Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
        if (a! > b!){
            no_decrease_to_right = false
            break
        }
    }
    
    if !no_double && no_decrease_to_right {
        counter += 1
        res.append(i)
    }
}
print(counter)

res

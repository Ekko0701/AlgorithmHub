func findWinner(_ n: Int) -> String { 
    var dp = Array(repeating: "CY", count: n + 1)
    
    if n >= 1 { dp[1] = "SK" }
    if n >= 2 { dp[2] = "CY" }
    if n >= 3 { dp[3] = "SK" }
    
    if n >= 4 {
        for i in 4...n {
            if dp[i - 1] == "CY" || dp[i - 3] == "CY" {
                dp[i] = "SK" // 상대가 패배할 수밖에 없는 경우 상근이가 이김
            } else {
                dp[i] = "CY" // 상대가 항상 이기는 경우 상근이가 패배
            }
        }
    }

    return dp[n]
}

if let input = readLine(), let n = Int(input) { 
    print(findWinner(n))
}
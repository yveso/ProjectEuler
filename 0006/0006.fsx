
let sumOfSquares n =
    [1..n]
    |> Seq.map (fun x -> x * x)
    |> Seq.sum

let squaredSum n = 
    let x = n * (n+1) / 2
    x * x

let answer = squaredSum 100 - sumOfSquares 100

printfn "%d" answer
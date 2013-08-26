let isPrime n =
    if n > 1 then
        let bound = int (System.Math.Sqrt (float n))
        seq { 2 .. bound }       
        |> Seq.forall (fun x -> n % x <> 0)       
    else false

let primeSeq =
    let rec checkYieldPrime n =
        seq {
            if isPrime n then
                yield n
            yield! checkYieldPrime (n+1)
        }
    checkYieldPrime 2

let answer =
    primeSeq
    |> Seq.take 10001
    |> Seq.max

printfn "%d" answer
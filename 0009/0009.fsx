let square n = n * n
let first (a, _, _) = a
let second (_, b, _) = b
let third (_, _, c) = c

let isPythagoreanTriplet a b c =
    square a + square b = square c

let searchedTriplet =
    seq {
        for a = 1 to 1000 do
            for b = a to 1000 do
                let c = 1000 - a - b
                yield (a, b, c) }
    |> Seq.filter (fun (a, b, c) -> isPythagoreanTriplet a b c)
    |> Seq.head

let answer = first searchedTriplet * second searchedTriplet * third searchedTriplet

printfn "%d" answer
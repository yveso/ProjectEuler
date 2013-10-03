let answer = 
  (2I ** 1000).ToString().ToCharArray()
  |> Array.map (fun x -> ((int)x - 48))
  |> Array.sum

printfn "%d" answer
import System.IO (readFile)

filename :: String
filename = "input.txt"

slidingW :: Int -> [Int] -> [[Int]]
slidingW _ [] = []
slidingW n xs = take n xs : slidingW n (tail xs)

sw :: Int -> [Int] -> [[Int]]
sw n xs = filter ((== n) . length) $ slidingW n xs


countAscending :: [Int] -> Int
countAscending [] = 0
countAscending [x] = 0
countAscending (x:y:xs)
  | y>x = 1 + countAscending (y:xs)
  | otherwise = countAscending (y:xs)

solve :: String -> Int
solve str
  = countAscending
  $ fmap sum
  $ sw 3
  $ fmap read
  $ lines str

main :: IO ()
main = do
  string <- readFile filename
  let solution = solve string
  print solution

import System.IO (readFile)

filename :: String
filename = "input.txt"

countAscending :: [Int] -> Int
countAscending [] = 0
countAscending [x] = 0
countAscending (x:y:xs) = (if y>x then 1 else 0) + countAscending (y:xs)

solve :: String -> Int
solve str = countAscending $ fmap read $ lines str

main :: IO ()
main = do
  string <- readFile filename
  let solution = solve string
  print solution

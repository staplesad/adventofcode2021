import System.IO
import Data.Function
import Data.List

filename :: String
filename = "input.txt"

splitOn :: Eq a => a -> [a] -> [[a]]
splitOn _ [] = []
splitOn c xs = takeWhile (/= c) xs : case dropWhile (/= c) xs of
    [] -> []
    [x] -> [[]]
    (x: xs') -> splitOn c xs'

parseCrabs :: String -> [Int]
parseCrabs = fmap read . splitOn ','

possibleHeights :: [Int] -> [Int]
possibleHeights xs = [minimum xs .. maximum xs]

getCost :: Int -> Int
getCost n = (n * (n+1)) `div` 2
--getCost n = sum [1..n]

calculateFuel :: [Int] -> Int -> Int
calculateFuel pos h = sum $ map (getCost . abs . subtract h) pos

minFuel :: [Int] -> Int
minFuel pos = minimum $ map (calculateFuel pos) $ possibleHeights pos

main :: IO ()
main = do
  input <- readFile filename
  let init = parseCrabs input
  print $ minFuel init

import System.IO
import Data.Function
import Data.Ord
import Data.List
import Data.Maybe (fromJust)

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

calculateFuel :: [Int] -> Int -> Int
calculateFuel pos h = sum $ map (abs . subtract h) pos

minFuel :: [Int] -> Int
minFuel pos = minimum $ map (calculateFuel pos) $ possibleHeights pos

main :: IO ()
main = do
  input <- readFile filename
  let init = parseCrabs input
  print $ minFuel init

import System.IO
import Data.Function

filename :: String
filename = "test.txt"

splitOn :: Eq a => a -> [a] -> [[a]]
splitOn _ [] = []
splitOn c xs = takeWhile (/= c) xs : case dropWhile (/= c) xs of
    [] -> []
    [x] -> [[]]
    (x: xs') -> splitOn c xs'

parseN :: String -> [Int]
parseN = fmap read . splitOn ','

parseB :: [String] -> [[[Int]]]
parseB [] = []
parseB xs = fmap ((fmap read) . words) (take 5 xs) : parseB (drop 5 xs)

main :: IO ()
main = do
  handle <- openFile filename ReadMode
  numbers <- hGetLine handle
  let parsedNumbers = parseN numbers
  _ <- hGetLine handle
  boards <- hGetContents handle
  let parsed = parseB $ filter (/= "") $ lines boards
  print parsedNumbers
  print parsed
  --let solution = solve parsedNumbers parsed
  --print solution

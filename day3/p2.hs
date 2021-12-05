import System.IO (readFile)
import Data.Char (digitToInt)
import Data.Function
import Data.List (transpose)

filename :: String
filename = "test.txt"

strToList :: String -> [Int]
strToList [] = []
strToList (x:xs) = (digitToInt x) : (strToList xs)

getLists :: String -> [[Int]]
getLists str =  fmap strToList $ lines str

addTuple :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuple a b = (fst a + fst b, snd a + snd b)

toDec :: Int -> [Int] -> Int
toDec _ [] = 0
toDec n a = (last a) * 2 ^ n + (toDec (n+1) (init a))

getNCount :: Int -> [Int] -> Int
getNCount n xs = length $ filter (==n) xs


oxygen :: [[Int]] -> [Int]
oxygen [] = error "missed soln"
oxygen [x] = x
oxygen xs =  let
  col = head $ transpose xs
  max = if getNCount 0 col > getNCount 1 col then 0 else 1
  remaining = filter (\x -> (head x) == max) xs
  in
  max : (oxygen $ fmap tail remaining)


co2 :: [[Int]] -> [Int]
co2 [] = error "missed soln"
co2 [x] = x
co2 xs =  let
  col = head $ transpose xs
  min = if getNCount 0 col > getNCount 1 col then 1 else 0
  remaining = filter (\x -> head x==min) xs
  in
  min : (co2 $ fmap tail remaining)

solve :: [[Int]] -> (Int, Int)
solve ints =  (toDec 0 $ oxygen ints, toDec 0 $ co2 ints)

main :: IO ()
main = do
  string <- readFile filename
  let parsed = getLists string
  let solution = solve parsed
  print solution
--  print $ (fst solution) * (snd solution)

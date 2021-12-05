import System.IO (readFile)
import Data.Char (digitToInt)
import Data.Function
import Data.List (transpose)

filename :: String
filename = "input.txt"

strToList :: String -> [Int]
strToList [] = []
strToList (x:xs) = (digitToInt x) : (strToList xs)

getLists :: String -> [[Int]]
getLists str =  fmap strToList $ lines str

addTuple :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuple a b = (fst a + fst b, snd a + snd b)

toDec :: Int -> ([Int], [Int]) -> (Int, Int)
toDec _ ([], []) = (0, 0)
toDec n (a, b) = addTuple ((last a) * 2 ^ n, (last b) *  2 ^ n) (toDec (n+1) (init a, init b))

getCounts :: [Int] -> (Int, Int)
getCounts [] = (0, 0)
getCounts (x:xs)
  | x == 1 = addTuple (0, 1) (getCounts xs)
  | x == 0 = addTuple (1, 0) (getCounts xs)
  | otherwise = error "not binary"

getDigit :: String -> (Int, Int) -> Int
getDigit "max" tup = if (fst tup) > (snd tup) then 0 else 1
getDigit "min" tup = if (fst tup) > (snd tup) then 1 else 0
getDigit _ _ = error "not a comp"

getM :: String -> [[Int]] -> [Int]
getM comp ints = fmap (getDigit comp) $ fmap getCounts ints


getTuple :: [[Int]] -> ([Int], [Int])
getTuple ints = (getM "max" (transpose ints), getM "min" (transpose ints))

solve :: String -> (Int, Int)
solve str
  = getLists str
  & getTuple
  & toDec 0

main :: IO ()
main = do
  string <- readFile filename
  let solution = solve string
  print solution
  print $ (fst solution) * (snd solution)

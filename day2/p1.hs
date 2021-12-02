import System.IO (readFile)
import Data.Function

filename :: String
filename = "input.txt"

getTuples :: String -> [(String, Int)]
getTuples str =  fmap (\[w, i] -> (w, read i)) $ fmap words $ lines str

addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples a b = (fst a + fst b, snd a + snd b)

getDim :: [(String, Int)] -> (Int, Int)
getDim [] = (0, 0)
getDim ((dir, mag):xs)
  | dir == "forward" = addTuples (mag, 0) (getDim xs)
  | dir == "up" = addTuples (0, -mag) (getDim xs)
  | dir == "down" = addTuples (0, mag) (getDim xs)

solve :: String -> (Int, Int)
solve str
  = getTuples str
  & getDim

main :: IO ()
main = do
  string <- readFile filename
  let solution = solve string
  print solution
  print $ (fst solution) * (snd solution)

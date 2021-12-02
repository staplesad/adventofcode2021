import System.IO (readFile)
import Data.Function

filename :: String
filename = "input.txt"

getTuples :: String -> [(String, Int)]
getTuples str =  fmap (\[w, i] -> (w, read i)) $ fmap words $ lines str

addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples a b = (fst a + fst b, snd a + snd b)

getDim :: Int -> [(String, Int)] -> (Int, Int)
getDim _ [] = (0, 0)
getDim aim ((dir, mag):xs)
  | dir == "forward" = addTuples (mag, mag*aim) (getDim aim xs)
  | dir == "up" = getDim (aim - mag) xs
  | dir == "down" = getDim (aim + mag) xs

solve :: String -> (Int, Int)
solve str
  = getTuples str
  & getDim 0

main :: IO ()
main = do
  string <- readFile filename
  let solution = solve string
  print solution
  print $ (fst solution) * (snd solution)

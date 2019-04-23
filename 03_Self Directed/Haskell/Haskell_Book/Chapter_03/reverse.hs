module Reverse where

rvrs :: String -> String
rvrs s = newWords
    where firstWord = take 5 s
          remainingWords = drop 6 s
          secondWord = take 2 remainingWords
          thirdWord = drop 3 remainingWords
          newWords = thirdWord ++ " " ++ secondWord ++ " " ++ firstWord

main :: IO ()
main = print $ rvrs "Curry is awesome"
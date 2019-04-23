module Print3 where

myGreeting :: String
myGreeting = "hello" ++ " world!"

hello :: String
hello = "hello"

world :: String
world = "world!"

main :: IO ()
main = do
    putStrLn myGreeting
    putStrLn secondGreeting
    where secondGreeting = concat [hello, " ", world]

thirdLetter :: String -> Char
thirdLetter x = x !! 2

-- letterIndex :: Int, String -> Char
letterIndex x s = s !! x

rvrs :: String -> String
rvrs s = newWords
    where firstWord = take 5 s
          remainingWords = drop 6 s
          secondWord = take 2 remainingWords
          thirdWord = drop 3 remainingWords
          newWords = thirdWord ++ " " ++ secondWord ++ " " ++ firstWord
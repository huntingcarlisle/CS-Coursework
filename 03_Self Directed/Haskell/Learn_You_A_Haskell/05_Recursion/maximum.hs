module Maximum where

    maximum' :: (Ord a) => [a] -> a
    maximum' [] = error "maximum of empty list"
    maximum' [x] = x
    maximum' (x:xs) = max x (maximum' xs)
        -- | x > maxTail = x
        -- | otherwise = maxTail
        -- where maxTail = maximum' xs

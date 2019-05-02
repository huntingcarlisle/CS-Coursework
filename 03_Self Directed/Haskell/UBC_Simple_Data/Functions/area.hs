module Area where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (area' 5) 25
                print $check_expect' (area' 1.5) (1.5 * 1.5)
    
    
    area' :: (Floating a) => a -> a
    -- given length of one side of square, return the area of square
    
    -- area' s = 0   -- stub
    area' = (**2)

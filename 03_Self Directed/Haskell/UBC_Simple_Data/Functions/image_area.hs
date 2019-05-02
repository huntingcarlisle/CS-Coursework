module ImageArea where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (image_area' 5) 25
                print $check_expect' (image_area' 1.5) (1.5 * 1.5)
    
    
    image_area' :: (Num a) => a -> a
    -- given length of one side of square, return the area of square
    
    -- image_area' s = 0   -- stub
    image_area' s = (*) s s
module Cartesian where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (cartesian' (0,1) (0,0)) 1
                print $check_expect' (cartesian' (0,-1) (0,0)) 1
                print $check_expect' (cartesian' (1,1) (0,0)) (sqrt 2)
                print $check_expect' (cartesian' (0,4) (4,0)) (sqrt 32)
    
    
    cartesian' :: Floating a => (a,a) -> (a,a) -> a
    -- calculate distance between two points
    
    -- cartesian' pointOne pointTwo = 0     --STUB
    cartesian' pointOne pointTwo = sqrt ((+)  
                                          ((*) 
                                             ((-) (fst pointOne) (fst pointTwo)) 
                                             ((-) (fst pointOne) (fst pointTwo)))
                                          ((*) 
                                             ((-) (snd pointOne) (snd pointTwo))
                                             ((-) (snd pointOne) (snd pointTwo))))
                        
    
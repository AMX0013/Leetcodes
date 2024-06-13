impl Solution {
    pub fn construct_product_matrix(mut grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (Y, X, modulo) = (grid.len(), grid[0].len(), 12345u128  );

        let (mut prefix_arr, mut i) = (vec![1; Y*X+1] , 1);
        // prefix_arr of 1s. has 1 extra pos to store the necessarray element 1
        // eats from left
        for y in 0 .. Y {
            for x in 0 .. X {
                prefix_arr[i] = ( prefix_arr[i-1]  * grid[y][x] as u128  )% modulo ;
                i+=1;
            }
        }

        let (mut suffix_arr, mut i) = (vec![1; Y*X+1] , Y*X);
        // prefix_arr of 1s. has 1 extra pos to store the necessarray element 1
        // eats from right
        for y in (0 .. Y).rev() {
            for x in (0 .. X).rev() {
                i-=1;
                suffix_arr[i] = ( suffix_arr[i+1]  * grid[y][x] as u128  )% modulo ;
                
            }
        }

        let mut i = 0;

        for y in 0..Y {
            for x in 0..X {
                grid[y][x] = ((prefix_arr[i] * suffix_arr[i+1]) % modulo) as i32;
                i+=1;
            }
        }
        return grid;
    }
}
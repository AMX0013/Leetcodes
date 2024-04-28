class Solution {
    public String addSpaces(String s, int[] spaces) {
        int n = s.length() + spaces.length;
        char[] res = new char[n];
        System.out.println(res);
        
        int s_idx = 0;
        int res_idx=0;

        for (int space_idx: spaces){

            while (s_idx < space_idx){
                res[res_idx++] = s.charAt(s_idx++);

            }
            res[res_idx++] = ' ';
            // System.out.println(res);
        }
        // finish rest of the tring
        while (s_idx < s.length())
        {
                res[res_idx++] = s.charAt(s_idx++);
                
        }
        // System.out.println(res);

        return String.valueOf(res);
    }
}
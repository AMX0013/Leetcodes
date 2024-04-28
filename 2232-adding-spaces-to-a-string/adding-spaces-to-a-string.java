class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder res = new StringBuilder(s);
        int times = 0;
        for(int index: spaces){
            res.insert(index+times++, ' ');
            
        }
        return res.toString();
    }
}
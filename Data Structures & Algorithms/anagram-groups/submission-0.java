class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        List<List<String>> result = new ArrayList<>();

        for (String string : strs) {
            char[] charArr = string.toCharArray();
            Arrays.sort(charArr);
            String sorted = new String(charArr);
            if (map.containsKey(sorted)) {
                map.get(sorted).add(string);
            } else {
                List<String> temp = new ArrayList<>();
                temp.add(string);
                map.put(sorted, temp);
            }
        }
        for (String list : map.keySet()) {
            result.add(map.get(list));
        }
        return result;
    }
}

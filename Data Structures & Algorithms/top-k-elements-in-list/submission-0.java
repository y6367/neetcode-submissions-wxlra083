class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int[] result = new int[k];
        int[] freq = new int[k];

        Arrays.fill(freq, -1);

        for (int num : map.keySet()) {
            int count = map.get(num);

            for (int i = 0; i < k; i++) {
                if (freq[i] == -1 || count > freq[i]) {

                    // shift down to make room
                    for (int j = k - 1; j > i; j--) {
                        freq[j] = freq[j - 1];
                        result[j] = result[j - 1];
                    }

                    freq[i] = count;
                    result[i] = num;
                    break;
                }
            }
        }

        return result;
    }
}

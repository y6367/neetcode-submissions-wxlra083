class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                if (result < (prices[j] - prices[i])) {
                    result = prices[j] - prices[i];
                }
            }
        }
        return result;
    }
}

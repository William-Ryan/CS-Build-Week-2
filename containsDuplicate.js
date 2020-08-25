var containsDuplicate = function(nums) {
    let num_set = new Set(nums);
    return (num_set.size < nums.length);
};
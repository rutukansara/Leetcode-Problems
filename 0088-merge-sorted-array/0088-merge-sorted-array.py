class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = []

        for i in range(len(nums2)):
            nums1.append(nums2[i])

        for i in range(len(nums1) - 1):
            for j in range(len(nums1) - 1 - i):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
        return nums1
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    
    min_heap = []
    
    heapq.heappush(min_heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= min_heap[0]:
            heapq.heappop(min_heap)
            
        heapq.heappush(min_heap, intervals[i][1])
        
    return len(min_heap)

if __name__ == "__main__":
    meetings = [[0, 30], [5, 10], [15, 20]]
    rooms = min_meeting_rooms(meetings)
    print(f"Minimum rooms required: {rooms}")
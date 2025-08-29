import heapq

# Class để đại diện cho một node trong cây nhị phân
class Node:
    def __init__(self, level, value, weight, bound, chosen):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.chosen = chosen

    # Hàm so sánh các node dựa trên giá trị bound (cận dưới)
    def __lt__(self, other):
        return self.bound > other.bound  # Max-heap theo bound


# Hàm tính cận trên cho bài toán Knapsack
def bound(node, W, values, weights, n):
    if node.weight >= W:
        return 0
    else:
        result = node.value
        total_weight = node.weight
        level = node.level + 1
        while level < n and total_weight + weights[level] <= W:
            total_weight += weights[level]
            result += values[level]
            level += 1
        if level < n:
            result += (W - total_weight) * values[level] / weights[level]
        return result


# Hàm giải bài toán Knapsack sử dụng thuật toán cắt tỉa
def knapsack(W, values, weights, n):
    # Sắp xếp các món đồ theo mật độ giá trị/trọng lượng giảm dần
    items = sorted([(values[i] / weights[i], values[i], weights[i]) for i in range(n)], reverse=True)
    
    # Khởi tạo priority queue (heap) để duyệt qua các node
    pq = []
    
    # Khởi tạo node gốc
    root = Node(-1, 0, 0, bound(Node(-1, 0, 0, 0, []), W, values, weights, n), [])
    heapq.heappush(pq, root)
    
    best_value = 0
    best_items = []
    nodes_expanded = 0

    while pq:
        node = heapq.heappop(pq)
        nodes_expanded += 1
        
        # Nếu node có giá trị lớn hơn giá trị tốt nhất hiện tại, cập nhật
        if node.value > best_value:
            best_value = node.value
            best_items = node.chosen
        
        # Duyệt qua 2 nhánh: chọn món đồ và không chọn món đồ
        if node.level + 1 < n:
            # Nhánh 1: Chọn món đồ tiếp theo
            next_item = node.level + 1
            if node.weight + weights[next_item] <= W:
                chosen = node.chosen + [next_item]
                next_node = Node(next_item, node.value + values[next_item], node.weight + weights[next_item],
                                 bound(Node(next_item, node.value + values[next_item], node.weight + weights[next_item], 0, chosen), W, values, weights, n), chosen)
                if next_node.bound > best_value:
                    heapq.heappush(pq, next_node)
            
            # Nhánh 2: Không chọn món đồ tiếp theo
            next_node = Node(next_item, node.value, node.weight, bound(Node(next_item, node.value, node.weight, 0, node.chosen), W, values, weights, n), node.chosen)
            if next_node.bound > best_value:
                heapq.heappush(pq, next_node)

    return best_value, best_items, nodes_expanded


# Ví dụ sử dụng:
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

best_value, best_items, nodes_expanded = knapsack(W, values, weights, n)

print(f"Giá trị tốt nhất: {best_value}")
print(f"Những món đồ đã chọn (chỉ số): {best_items}")
print(f"Số lượng node đã duyệt: {nodes_expanded}")

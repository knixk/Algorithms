int count = 0, current_factor = a.get(size() - 1), flag;
while (current_factor <= b.get(0)) {
    flag = 0;
    for (int i = 0; i < a.size(); i++) {
        if (current_factor % a.get(i) != 0) {
            flag = 1;
            break;
        }
    }
    if (flag == 0) {
        for (int i = 0; i < b.size(); i++) {
            if (b.get(i) % current != 0) {
                flag = 1;
                break;
            }
        }
    }
    if (flag == 0) {
        count++;
    }
    current_factor++;
}
return count;

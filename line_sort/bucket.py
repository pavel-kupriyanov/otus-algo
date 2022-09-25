def bucket_sort(arr: list[int]):
    max_item = max(arr)
    buckets = [... for _ in arr]

    for item in arr:
        position = (item * len(arr)) // (max_item + 1)
        if isinstance(buckets[position], int):
            buckets[position] = [buckets[position], item]
        elif isinstance(buckets[position], list):
            buckets[position].append(item)
        else:
            buckets[position] = item

    index = 0
    for bucket in buckets:
        if isinstance(bucket, list):
            bucket = sorted(bucket)
            for item in bucket:
                arr[index] = item
                index += 1
        elif isinstance(bucket, int):
            arr[index] = bucket
            index += 1

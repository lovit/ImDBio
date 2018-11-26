class ReviewsReader:

    def __init__(self, csv_path, yield_idx=True, yield_title=True, num_review=-1):
        self.path = csv_path
        self.yield_idx = yield_idx
        self.yield_title = yield_title
        self.num_review = num_review
        self._len = 0

    def __len__(self):
        if self._len == 0:
            for i, _ in enumerate(self):
                continue
            self._len = i + 1
        return self._len

    def __iter__(self):
        with open(self.path, encoding='utf-8') as f:
            for i, doc in enumerate(f):
                # check count
                if self.num_review > 0 and i >= self.num_review:
                    break
                idx, title, text = doc[:-1].split('\t', 2)
                # yield format
                if self.yield_idx and self.yield_title:
                    yield (idx, title, text)
                elif self.yield_idx and not self.yield_title:
                    yield (idx, text)
                elif not self.yield_idx and not self.yield_title:
                    yield text
                else:
                    yield (title, text)
        self._len = i + 1
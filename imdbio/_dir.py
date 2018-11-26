from glob import glob

class ReviewDirectoryReader:

    def __init__(self, directory, yield_idx=True, yield_title=True, num_review=-1):
        self.directory = directory
        self.paths = sorted(glob(self.directory + '/*.txt'), key=lambda x:int(x.split('/')[-1][:-4]))
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
        count = 0
        for path in self.paths:
            # parse idx
            idx = path.split('/')[-1][:-4]

            # check count
            if self.num_review > 0 and count >= self.num_review:
                break
            with open(path, encoding='utf-8') as f:
                docs = [doc[:-1].split('\t', 1) for doc in f]
            if (self.num_review > 0) and (len(docs) + count > self.num_review):
                docs = docs[:self.num_review - count - 1]
            count += len(docs)

            # yield format
            if self.yield_idx and self.yield_title:
                docs = [(idx, doc[0], doc[1]) for doc in docs]
            elif self.yield_idx and not self.yield_title:
                docs = [(idx, doc[1]) for doc in docs]
            elif not self.yield_idx and not self.yield_title:
                docs = [doc[1] for doc in docs]

            # yield
            for row in docs:
                yield row

        self._len = count
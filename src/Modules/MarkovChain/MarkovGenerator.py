import random

class MarkovGenerator:
    def __init__(self):
        self.probs_ob = {}
        self.markov_ob = {}
        self.seeds_lengths = []
        self.seeds_ar = []
        self.min_word_length = 0
        self.max_word_length = 30
        
        self.settings = {"must_create_only_new_names": True, "must_keep_sample_length": True}

    def init(self, ar):
        self.seeds_lengths = []
        self.seeds_ar = ar.copy()

        self.probs_ob = {}
        for i in range(len(self.seeds_ar)):
            string = self.seeds_ar[i]
            prev_prev_ch = "|"
            prev_ch = "|"

            for j in range(len(string) + 1):
                if j < len(string):
                    ch = string[j]
                else:
                    ch = "|"

                if prev_prev_ch in self.probs_ob:
                    ob = self.probs_ob[prev_prev_ch]
                else:
                    ob = {}
                    self.probs_ob[prev_prev_ch] = ob

                if prev_ch in ob:
                    ob2 = ob[prev_ch]
                else:
                    ob2 = {}
                    ob[prev_ch] = ob2

                if ch in ob2:
                    ob2[ch] += 1
                else:
                    ob2[ch] = 1

                prev_prev_ch = prev_ch
                prev_ch = ch

            while len(self.seeds_lengths) <= len(string):
                self.seeds_lengths.append(0)

            self.seeds_lengths[len(string)] += 1

        self.markov_ob = {}
        for ch1 in self.probs_ob:
            ob2 = self.probs_ob[ch1]
            for ch2 in ob2:
                ob3 = ob2[ch2]
                chars_ar = []
                weight_ar = []
                for ch3 in ob3:
                    chars_ar.append(ch3)
                    weight_ar.append(ob3[ch3])
                self.markov_ob[ch1 + ch2] = {"chars_ar": chars_ar, "weight_ar": weight_ar}

        perc_val = 0.025
        perc_num = round(perc_val * len(self.seeds_ar))

        id_val = 0
        sum_val = 0
        while sum_val < perc_num:
            sum_val += self.seeds_lengths[id_val]
            id_val += 1

        self.min_word_length = id_val - 1

        id_val = len(self.seeds_lengths) - 1
        sum_val = 0
        while sum_val < perc_num:
            sum_val += self.seeds_lengths[id_val]
            id_val -= 1

        self.max_word_length = id_val + 1

    def generate(self):
        num_attempts = 0
        must_make_next_attempt = True

        while must_make_next_attempt:
            must_make_next_attempt = False
            num_attempts += 1

            res = ""
            prev_prev_ch = "|"
            prev_ch = "|"
            need_1_more = True

            while need_1_more:
                ob = self.markov_ob.get(prev_prev_ch + prev_ch, None)

                if ob:
                    id_val = self.get_random_index_from_weighted_ar(ob["weight_ar"])
                    ch = ob["chars_ar"][id_val]

                    if ch != "|":
                        res += ch
                    else:
                        need_1_more = False

                    prev_prev_ch = prev_ch
                    prev_ch = ch

            if num_attempts < 10:
                if self.settings["must_create_only_new_names"]:
                    if res in self.seeds_ar:
                        must_make_next_attempt = True

                if not must_make_next_attempt:
                    if self.settings["must_keep_sample_length"]:
                        if not (self.min_word_length <= len(res) <= self.max_word_length):
                            must_make_next_attempt = True

        return res

    def get_random_index_from_weighted_ar(self, ar):
        if len(ar) == 1:
            if ar[0] == 0:
                return -1
            else:
                return 0

        res = -1
        s = sum(ar)

        if s > 0:
            rnd = s * random.random()
            rid = 0

            while rnd >= ar[rid]:
                rnd -= ar[rid]
                rid += 1

            res = rid
        else:
            res = -1

        return res
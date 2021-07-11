import pandas as pd
import random

def recite_yin(initial_list, vowel_list = ['a', 'i', 'u', 'e', 'o'], df=None):
    '''
    Parameters
    ----------
    df: None or Dataframe
        A df which contains all fifty yin
        If df is None default read the following table
            initial	a	i	u	e	o	type
        0	empty	ア	イ	ウ	エ	オ	hard
        1	k	カ	キ	ク	ケ	コ	hard
        2	s	サ	シ	ス	セ	ソ	hard
        3	t	タ	チ	ツ	テ	ト	hard
        4	n	ナ	ニ	ヌ	ネ	ノ	hard
        5	h	ハ	ヒ	フ	ヘ	ホ	hard
        6	m	マ	ミ	ム	メ	モ	hard
        7	y	ヤ	NaN	ユ	NaN	ヨ	hard
        8	r	ラ	リ	ル	レ	ロ	hard
        9	w	ワ	ヰ	NaN	ヱ	ヲ	hard
        10	empty	あ	い	う	え	お	soft
        11	k	か	き	く	け	こ	soft
        12	s	さ	し	す	せ	そ	soft
        13	t	た	ち	つ	て	と	soft
        14	n	な	に	ぬ	ね	の	soft
        15	h	は	ひ	ふ	へ	ほ	soft
        16	m	ま	み	む	め	も	soft
        17	y	や	NaN	ゆ	よ	NaN	soft
        18	r	ら	り	る	れ	ろ	soft
        19	w	わ	ゐ	NaN	ゑ	を	soft
    initial_list: list
        A list to choose initial from
        e.g. ['empty', 'k]
    vowel_list: list
        A list to choose vowel from
        default: ['a', 'i', 'u', 'e', 'o']
    '''
    if df is None:
        df = pd.read_csv('fifty_yin.csv')
    initial = random.sample(initial_list, 1)[0]
    vowel = random.sample(vowel_list, 1)[0]
    if initial == 'empty':
        print(f'Please write the two types of yin which spells {vowel}: ')
    else:
        print(f'Please write the two types of yin which spells {initial}{vowel}: ')

    # wait for Enter to show the answer
    key = None
    while key != '':
        key = input("Press Enter to show the answer... ")
    
    print(df.loc[df['initial'] == initial, vowel])

------------------------

v_blend: 予測値のばらつきが大きい場合に適応的に対応したい場合
h_blend: よりシンプルで直感的なアンサンブルが必要な場合

------------------------
[v_blend]

def v_blend(path_to_ds, file_short_names, dk):

    def read(dk,i):
        tnm = dk["subm"][i]["name"]
        FiN = dk["path"] + tnm + ".csv"
        return pd.read_csv(FiN).rename(columns={'target':tnm, dk["target"]:tnm})
        
    def merge(dfs_subm):
        df_subms = pd.merge(dfs_subm[0],  dfs_subm[1], on=[dk['id']])
        for i in range(2, len(dk["subm"])): 
            df_subms = pd.merge(df_subms, dfs_subm[i], on=[dk['id']])
        return df_subms
        
    def da(dk,sorting_direction):
        
        df_subms = merge([read(dk,i) for i in range(len(dk["subm"]))])
        cols = [col for col in df_subms.columns if col != dk['id']]
        short_name_cols = [c for c in cols]
        
        def alls(x, sd=sorting_direction,cs=cols):
            reverse = True if sd=='desc' else False
            tes = {c: x[c] for c in cs}.items()
            subms_sorted = [t[0] for t in sorted(tes,key=lambda k:k[1],reverse=reverse)]
            return subms_sorted
            
        def summa(x,cs,wts,ic_alls): 
            return sum([x[cs[j]] * (wts[0][j] + wts[1][ic_alls[j]]) for j in range(len(cs))])
            
        wts = [
            [[e['weight'] for e in dk["subm"]], [w for w in dk["subwts" ]]],
            [[e['weight'] for e in dk["subm2"]],[w for w in dk["subwts2"]]],
            [[e['weight'] for e in dk["subm3"]],[w for w in dk["subwts3"]]],
        ]
        def correct(x, cs=cols, wts=wts):
            i = [x['alls'].index(c) for c in short_name_cols]
            if   0.00 < x['mx-m'] <= 0.10: return summa(x,cs,wts[0],i)
            if   0.10 < x['mx-m'] <= 0.20: return summa(x,cs,wts[1],i)
            else:                          return summa(x,cs,wts[2],i)
                
        def amxm(x, cs=cols):
            list_values = x[cs].to_list()
            mxm = abs(max(list_values)-min(list_values))
            return mxm
            
        df_subms['mx-m']       = df_subms.apply(lambda x: amxm   (x), axis=1)
        df_subms['alls']       = df_subms.apply(lambda x: alls   (x), axis=1)
        df_subms[dk["target"]] = df_subms.apply(lambda x: correct(x), axis=1)
        schema_rename = { old_nc:new_shnc for old_nc, new_shnc in zip(cols, short_name_cols) }
        df_subms = df_subms.rename(columns=schema_rename)
        df_subms = df_subms.rename(columns={dk["target"]:"ensemble"})
        df_subms.insert(loc=1, column=' _ ', value=['   '] * len(df_subms))
        df_subms[' _ '] = df_subms[' _ '].astype(str)
        pd.set_option('display.max_rows',100)
        pd.set_option('display.float_format', '{:.4f}'.format)
        vcols = [dk['id']] + [' _ '] + short_name_cols + [' _ '] + ['mx-m'] + [' _ '] + ['alls'] + [' _ '] + ['ensemble']
        df_subms = df_subms[vcols]
        display(df_subms.head(5))
        pd.set_option('display.float_format', '{:.5f}'.format)
        df_subms = df_subms.rename(columns={"ensemble":dk["target"]})
        df_subms.to_csv(f'tida_{sorting_direction}.csv', index=False)
        return df_subms[[dk['id'],dk['target']]]
   
    def ensemble_da(dk): 
        dfD = da(dk,'desc')
        dfA = da(dk,'asc')
        dfA[dk['target']] = dk['desc'] * dfD[dk['target']] + \
                            dk['asc']  * dfA[dk['target']]
        return dfA
    
    return  ensemble_da(dk)


------------------------
[h_blend]

import pandas as pd

def h_blend(path, fs_names, params):
    dk = params
    
    def da(dk, sorting_direction):
        def read_subm(dk, i):
            tnm = dk["subm"][i]["name"]
            FiN = dk["path"] + tnm + ".csv"
            df = pd.read_csv(FiN)
            # targetカラムとdk["target"]カラムの名前をtnmに変更
            rename_dict = {}
            if 'target' in df.columns:
                rename_dict['target'] = tnm
            if dk["target"] in df.columns and dk["target"] != 'target':
                rename_dict[dk["target"]] = tnm
            return df.rename(columns=rename_dict)
        
        # 全てのサブミッションファイルを読み込み
        dfs_subm = [read_subm(dk, i) for i in range(len(dk["subm"]))]
        
        # 最初の2つのデータフレームをマージ
        df_subms = pd.merge(dfs_subm[0], dfs_subm[1], on=[dk['id']])
        
        # 残りのデータフレームを順次マージ
        for i in range(2, len(dk["subm"])): 
            df_subms = pd.merge(df_subms, dfs_subm[i], on=[dk['id']])
        
        # IDカラム以外のカラムを取得
        cols = [col for col in df_subms.columns if col != dk['id']]
        short_name_cols = [c for c in cols]
        corrects = [wt for wt in dk["subwts"]]
        weights = [subm['weight'] for subm in dk["subm"]]
        
        def alls(x, sd=sorting_direction, cs=cols):
            reverse = True if sd == 'desc' else False
            # 各カラムの値でソート
            tes = {c: x[c] for c in cs}.items()
            subms_sorted = [t[0] for t in sorted(tes, key=lambda item: item[1], reverse=reverse)]
            return subms_sorted
        
        def correct(x, cs=cols, w=weights, cw=corrects):
            # 各カラムのインデックスを取得
            ic = [x['alls'].index(c) for c in short_name_cols]
            # 重み付き計算
            cS = [x[cols[j]] * (w[j] + cw[ic[j]]) for j in range(len(cols))]
            return sum(cS)
        
        # allsカラムを追加
        df_subms['alls'] = df_subms.apply(lambda x: alls(x), axis=1)
        # ターゲットカラムを追加
        df_subms[dk["target"]] = df_subms.apply(lambda x: correct(x), axis=1)
        
        # カラム名を変更
        schema_rename = {old_nc: new_shnc for old_nc, new_shnc in zip(cols, short_name_cols)}
        df_subms = df_subms.rename(columns=schema_rename)
        df_subms = df_subms.rename(columns={dk["target"]: "ensemble"})
        
        # セパレータカラムを追加
        df_subms.insert(loc=1, column=' * ', value=['   '] * len(df_subms))
        df_subms[' * '] = df_subms[' * '].astype(str)
        
        # 表示設定
        pd.set_option('display.max_rows', 8)
        pd.set_option('display.float_format', '{:.4f}'.format)
        
        # 表示用のカラム順序
        vcols = [dk['id']] + [' * '] + short_name_cols + [' * '] + ['alls'] + [' * '] + ['ensemble']
        df_subms = df_subms[vcols]
        
        # 最初の5行を表示
        print(df_subms.head(5))
        
        # 表示形式を変更
        pd.set_option('display.float_format', '{:.5f}'.format)
        df_subms = df_subms.rename(columns={"ensemble": dk["target"]})
        
        # CSVファイルに出力
        df_subms.to_csv('tida_alls.csv', index=False)
        
        return df_subms
    
    # サンプルサブミッションファイルを読み込み
    sample_subm = pd.read_csv(path + fs_names[1] + ".csv")
    
    def ensemble_da(dk, submission=sample_subm): 
        _id, target, d, a = dk['id'], dk['target'], dk['desc'], dk['asc']
        
        # 降順でのアンサンブル
        dfs = da(dk, 'desc')
        dfD = dfs[[_id, target]]
        dfD.to_csv('tida_desc.csv', index=False)
        
        # 昇順でのアンサンブル
        dfs = da(dk, 'asc')
        dfA = dfs[[_id, target]]
        dfA.to_csv('tida_asc.csv', index=False)
        
        # 最終的なアンサンブル結果
        submission[target] = dfD[target] * d + a * dfA[target]
        
        return submission
    
    result = ensemble_da(dk)
    
    return result

-----------------------


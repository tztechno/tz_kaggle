################################
#after
dls = ImageDataLoaders.from_df(train_df,
                               fn_col=0, #path
                               label_col=1, # マッピング前の文字列を含むカラム
                               valid_pct=0.2,
                               folder='',
                               item_tfms=Resize(100),
                               label_delim=None, # マルチラベルの場合はNoneに設定
                               y_block=CategoryBlock(vocab=train_df['label'].unique()) # マッピング前の文字列を含むカラムのユニークな値をvocabに設定
                              )
dls.show_batch(max_n=16) # マッピング前の文字列を含むカラムのユニークな値をラベルとして表示


################################
#before
dls = ImageDataLoaders.from_df(train_df, 
                               fn_col=0, #path
                               label_col=1,
                               valid_pct=0.2,
                               folder='', 
                               item_tfms=Resize(100))
dls.show_batch(max_n=16)

################################

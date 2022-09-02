from config.config import Config
from config.utils import get_now


class Target():

    def __init__(self, config):
        self.config = config


    # def s3_csv(self, df, start_date, bucket, dst_path, file_path, file_name):
    #     '''
    #     Save data to s3
    #     '''        
    #     start_date = get_date_str(start_date)
    #     if len(df) > 0:
    #         os.makedirs('data', exist_ok=True)
    #         file_name = f'{start_date}_{file_path}_{file_name}'
    #         dst_path_file = f'{dst_path}/{start_date[0:4]}/{start_date[5:7]}'
            
    #         df.to_csv(f'data/{file_name}.csv', index=False, sep=';', header=False)
    #         zip_file(f'data/{file_name}', self.config.file_zip_pwd)
    #         if not Config.env == 'test':
    #             bucket = bucket.replace('s3a://', '').replace('s3n://', '')
    #             self.upload_to_s3('data', bucket, file_name, dst_path_file)
                
    #     print(get_now(), "-", f'{start_date}_{file_name}.csv', '- count:', len(df))

    #     return df

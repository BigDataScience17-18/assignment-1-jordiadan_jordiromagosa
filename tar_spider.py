import scrapy
import os
import urllib
import tarfile
import gzip

from process_files import process_file


def create_project_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def extract(tar_url, extract_path='.'):
    file_tmp = urllib.urlretrieve(tar_url, filename=None)[0]
    tar = tarfile.open(file_tmp)
    for member in tar.getmembers():
        if member.name.find('.gz') == -1 and not os.path.exists(extract_path + member.name):
            os.makedirs(extract_path + member.name)
        f = tar.extractfile(member)
        if f is not None:
            # read .gz file with gzip
            content = gzip.GzipFile(fileobj=f).read()
            file_name = str.replace(extract_path + member.name, '.gz', '')

            # write output file
            f_out = open(file_name, 'w')
            f_out.write(content)
            f_out.close()
            process_file(file_name)

    tar.close()

    # start data processing


class TarDownloader(scrapy.Spider):
    name = 'tar_dowloader'
    download_directory = 'files/'
    result_directory = 'results/'
    # domain URL
    allowed_domains = ['https://archive.ics.uci.edu/ml/machine-learning-databases/eeg-mld/eeg_full/']
    # links to the specific pages
    start_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/eeg-mld/eeg_full/']

    def parse(self, response):
        files_extracted = response.xpath('//table/tr/td/a/@href').extract()
        self.logger.info('Number of files: %i', len(files_extracted))
        for href in files_extracted:
            if href[-6:] == 'tar.gz':
                path = response.urljoin(href)
                self.logger.info('%s', path)
                yield scrapy.Request(
                    url=path,
                    callback=self.download_tar(path)
                )

    def download_tar(self, path):
        create_project_directory(self.download_directory)
        create_project_directory(self.result_directory)
        extract(path, self.download_directory)

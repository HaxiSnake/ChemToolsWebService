# coding: utf-8
from subprocess import check_call
from os.path import join

from .config import CALCULATE_CMD_TYPE, CALCULATE_DATA_PATH
from utils import chemistry_logger


class MopacModel():
    def __init__(self, mop_fname_list):
        self.mop_fname_list_no_ext = []

        for fname in mop_fname_list:
            name = fname.split('.')[0]
            self.mop_fname_list_no_ext.append(name)

    def opt4dragon(self, model_name):
        for name in self.mop_fname_list_no_ext:
            mol_path = join(CALCULATE_DATA_PATH.DRAGON, model_name, name,
                            '%s.mol' % name)
            mop_path = join(CALCULATE_DATA_PATH.MOPAC, model_name, name,
                            '%s.mop' % name)
            out_path = join(CALCULATE_DATA_PATH.MOPAC, model_name, name,
                            '%s.out' % name)

            cmd = '%s "%s"' % (CALCULATE_CMD_TYPE.MOPAC, mop_path)
            chemistry_logger.info('opt4dragon part1 cmd: %s' % cmd)
            check_call(cmd, shell=True)

            # get the optimized orientation in out file and replace counterpart
            # in mol file with it now orientation_info
            # is filed with optimized orientationn

            cmd = 'obabel -imoo "%s" -omol -O "%s" --gen3D' % (out_path,
                                                               mol_path)
            chemistry_logger.info('opt4dragon part2 cmd: %s' % cmd)
            check_call(cmd, shell=True)

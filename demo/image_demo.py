# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser

from mmseg.apis import inference_segmentor, init_segmentor, show_result_pyplot, show_result_pyplot2
from mmseg.core.evaluation import get_palette

import numpy as np


def main():
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument('--out-file', default=None, help='Path to output file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    #was 'cityscapes'
    parser.add_argument(
        '--palette',
        #default='ade',
        default='imaterialist_numclasses110',
        help='Color palette used for segmentation map')
    parser.add_argument(
        '--opacity',
        type=float,
        default=0.5,
        help='Opacity of painted segmentation map. In (0, 1] range.')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    model = init_segmentor(args.config, args.checkpoint, device=args.device)
    
    # test a single image
    result = inference_segmentor(model, args.img) #result = inference_segmentor(model, rescale1=False, args.img) result = model(return_loss=False, rescale=False, **data)
    
    #print(type(result))
    #print(result.size())
    
    print(type(result))
    arr_2 = np.array(result)
    print(arr_2.shape)
    
    list2 = show_result_pyplot2(
        model,
        args.img,
        result,
        get_palette(args.palette),
        opacity=args.opacity,
        out_file=args.out_file)
    
    print("\n\n palette.nshape[0] \n")
    print(list2[0])
    print("\n len(self.CLASSES) \n")
    print(list2[1])
    print("\n\n")
    
    # show the results
    show_result_pyplot(
        model,
        args.img,
        result,
        get_palette(args.palette),
        opacity=args.opacity,
        out_file=args.out_file)
    
    print(type(result))
    #print(result.size())
    arr_2 = np.array(result)
    print(arr_2.shape)


if __name__ == '__main__':
    main()

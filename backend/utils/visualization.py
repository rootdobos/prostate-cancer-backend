def get_intervals(model_name):
    match model_name:
        case "efficientnet_clam":
            return {
                "0": (-6, -4),
                "1": (-6, -3),
                "2": (-3.5, -0.5),
                "3": (-3, 0),
                "4": (-3, 0),
                "5": (-0.5, 1)
            }
        case "efficientnet_clamsimple":
            return {
                "0": (0, 3),
                "1": (-1, 3),
                "2": (-1, 3),
                "3": (-1, 2),
                "4": (0, 3),
                "5": (0, 3)
            }
        # case "efficientnet_clamsimplesigmoid":
        #     return {
        #         "0": (0.5, 1),
        #         "1": (0.5, 1),
        #         "2": (0.5, 1),
        #         "3": (0.5, 1),
        #         "4": (0.5, 1),
        #         "5": (0.5, 1)
        #     }
        case "efficientnet_clamsimplesigmoid":
            return {
                "0": (0, 1),
                "1": (0, 1),
                "2": (0, 1),
                "3": (0, 1),
                "4": (0, 1),
                "5": (0, 1)
            }
        case "resnext_clamsigmoid":
            return {
                "0": (-5, -2),
                "1": (-5, -2),
                "2": (-3, -1.8),
                "3": (-3, -1.8),
                "4": (-3, -1),
                "5": (-2.5, -1)
            }

import numpy as np


def crps(obs, predictions, nb_elements, df=None):
    crps_val = 0

    # Check input
    if len(predictions) < nb_elements:
        print("The required elements number is above the "
              "vector length in the score calculation.")
        exit()

    x = predictions[0:nb_elements]
    xObs = obs

    # Build the cumulative distribution function for the middle of the x
    # Parameters for the estimated distribution from Gringorten (a=0.44, b=0.12).
    # Choice based on Cunnane, C., 1978, Unbiased plotting positions, A review.
    irep = 0.44
    nrep = 0.12
    divisor = 1.0 / (nb_elements + nrep)

    if not df:
        x = np.sort(x)

        F_begin = (1 - irep) * divisor
        F_last = (nb_elements - irep) * divisor
        F = np.linspace(F_begin, F_last, num=nb_elements)

    else:
        p = x.argsort()
        x = x[p]
        df = df[p]
        F = np.zeros(len(x))
        for i in np.arange(len(x)):
            if i == 0:
                F[i] = -irep * divisor + df[i]
            else:
                F[i] = F[i - 1] + df[i]
        if F[len(x) - 1] > 1:
            print("Error: F[len(x)-1]=" + str(F[len(x) - 1]))
            exit()
        if F[len(x) - 1] < 0.8:
            print("Error: F[len(x)-1]=" + str(F[len(x) - 1]))
            exit()

    # Indices for the left and right part (according to xObs) of the distribution
    indLeftStart = 0
    indLeftEnd = 0
    indRightStart = nb_elements - 1
    indRightEnd = nb_elements - 1

    # Find FxObs, fix xObs and integrate beyond limits
    xObsCorr = xObs
    FxObs = 0

    if xObs <= x[0]:  # If xObs before the distribution
        indRightStart = 0
        FxObs = 0
        xObsCorr = x[indRightStart]
        crps_val = crps_val + (xObsCorr - xObs)
    elif xObs > x[nb_elements - 1]:  # If xObs after the distribution
        indLeftEnd = nb_elements - 1
        FxObs = 1
        xObsCorr = x[indLeftEnd]
        crps_val = crps_val + (xObs - xObsCorr)
    else:  # If xObs inside the distribution

        # Find the indices into a sorted array a such that,
        # if the corresponding elements in v were inserted
        # before the indices, the order of a would be preserved.
        rowInsert = np.searchsorted(x, xObs)
        indLeftEnd = rowInsert - 1
        indRightStart = indLeftEnd + 1
        if x[indRightStart] == x[indLeftEnd]:
            FxObs = (F[indLeftEnd] + F[indRightStart]) * 0.5
        else:
            FxObs = F[indLeftEnd] + (F[indRightStart] - F[indLeftEnd]) * (
                    xObs - x[indLeftEnd]) / (x[indRightStart] - x[indLeftEnd])

            # Integrate the CRPS around FxObs
            crps_val += (FxObs * FxObs - F[indLeftEnd] * F[indLeftEnd]) * (
                        xObsCorr - 0.5 * (x[indLeftEnd] + xObsCorr))  # Left
            crps_val += ((1 - FxObs) * (1 - FxObs) - (1 - F[indRightStart]) * (
                        1 - F[indRightStart])) * (
                                0.5 * (xObsCorr + x[indRightStart]) - xObsCorr)  # Right

    # Integrate on the left part below F(0). First slice from the bottom.
    crps_val = crps_val + (F[indLeftStart] * F[indLeftStart]) * (
            xObsCorr - x[indLeftStart])

    # Integrate on the left part
    F2 = F * F  # element-wise with arrays
    len_x = len(x)
    # x_aver = np.zeros(len_x) # CHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECK
    x_aver = x
    x_aver[0:len_x - 1] = 0.5 * (x[0:len_x - 1] + x[1:len_x])
    vectcrps = (F2[indLeftStart + 1:indLeftEnd + 1] - F2[indLeftStart:indLeftEnd]) * (
        xObsCorr - x_aver[indLeftStart:indLeftEnd])
    crps_val = crps_val + np.sum(vectcrps)
    # SLOWER:
    # for i in np.arange(indLeftStart,indLeftEnd):
    #    crps = crps+(F[i+1]*F[i+1]-F[i]*F[i])*(xObsCorr-0.5*(x[i]+x[i+1]))

    # Integrate on the right part
    mF = 1 - F
    mF2 = mF * mF
    vectcrps = (mF2[indRightStart:indRightEnd] -
                mF2[indRightStart + 1:indRightEnd + 1]) * (
                       x_aver[indRightStart:indRightEnd] - xObsCorr)
    crps_val = crps_val + np.sum(vectcrps)
    # SLOWER:
    # for i in np.arange(indRightStart,indRightEnd):
    #    crps = crps+((1.0-F[i])*(1.0-F[i])-(1.0-F[i+1])*
    #    (1.0-F[i+1]))*(0.5*(x[i]+x[i+1])-xObsCorr)

    # Integrate on the right part above F(indRightEnd). First slice from the bottom.
    crps_val = crps_val + ((1 - F[indRightEnd]) * (1 - F[indRightEnd])) * (
                x[indRightEnd] - xObsCorr)

    return crps_val


def crpss(obs, predictions, nb_elements, val_clim, df=None):
    if val_clim == 0:
        print("The value of the climatology is null !")

    # First process the CRPS and then the skill score
    crps_val = crps(obs, predictions, nb_elements, df)
    crpss_val = (crps_val - val_clim) / (0.0 - val_clim)

    return crpss_val

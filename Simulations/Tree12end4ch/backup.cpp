			if((isCoordinator || isClusterHead) && cfp_cont < (slotframesize-1)) { //31 -> two superframes (extract the 8 from the CAP)
				//trace() << "Indo para o update channel, final do slot " << cfp_cont;
				setTimer(UPDATE_CHANNEL_CFP, ((slotSize-1)/0.1));
			}
			else if(!(isCoordinator || isClusterHead) && cfp_cont < (slotframesize-2)) { //31 -> two superframes (extract the 8 from the CAP)
				//trace() << "Indo para o update channel, final do slot - end node " << cfp_cont;
				setTimer(UPDATE_CHANNEL_CFP, ((slotSize-1)/0.1));
			}
			else if(!isCoordinator) {
				//trace() << "Indo para o endfrae, final do slot " << cfp_cont;
				setTimer(END_FRAME, ((slotSize-2)/0.1));
			}